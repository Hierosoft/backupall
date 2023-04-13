'''
Compare two directories and place the added files from the second into
a  third.
'''
import sys
import os
import shutil
import filecmp


def echo0(*args):
    print(*args, file=sys.stderr)


def _diffnames(small_dir, big_dir, patch_dir, exclude_dotexts=None,
               delete_excluded=True):
    '''
    ^ If arguments are changed, copy them to recursive call!

    Do not call this directly (the diffnames method that calls this
    ensures that the small_dir and big_dir exist). See the diffnames
    (without the leading undercore) documentation instead.

    Keyword arguments:
    delete_excluded -- If True, any file in the destination (that is
        traversed--in other words, is in big) where the extension is
        exclude_dotexts will be deleted.
    '''
    files_added = 0
    for sub in os.listdir(big_dir):
        small_path = os.path.join(small_dir, sub)
        big_path = os.path.join(big_dir, sub)
        patch_path = os.path.join(patch_dir, sub)
        if not os.path.isdir(patch_dir):
            if not os.path.isdir(small_dir):
                # Do it here so copystat runs on every level regardless
                #   of whether this or a child directory has files not
                #   matching small. However, we can't tell the future
                #   so this will not work unless this directory also
                #   doesn't exist.
                # TODO: re-evaluate this logic.
                os.makedirs(patch_dir)
                shutil.copystat(big_dir, patch_dir)

        if os.path.isfile(big_path):
            if os.path.isfile(small_path):
                if filecmp.cmp(small_path, big_path, shallow=False):
                    # shallow=True only checks type date and size.
                    continue
            if not os.path.isdir(patch_dir):
                os.makedirs(patch_dir)
                shutil.copystat(big_dir, patch_dir)
            if os.path.islink(big_path):
                sym_dest = os.readlink(big_path)
                echo0('Warning: ln -s "{}" "{}"'
                      ''.format(sym_dest, big_path))
                os.symlink(sym_dest, patch_path)
            else:
                lower_dot_ext = os.path.splitext(patch_path.lower())[1]
                if ((exclude_dotexts is not None)
                        and (lower_dot_ext in exclude_dotexts)):
                    if delete_excluded:
                        if os.path.isfile(patch_path):
                            print('del "{}"'.format(patch_path))
                            os.remove(patch_path)
                    # else just ignore it (don't copy it either!)
                else:
                    files_added += 1
                    print('copy2 "{}" "{}"'.format(big_path, patch_path))
                    if not os.path.isfile(patch_path):
                        shutil.copy2(big_path, patch_path)
        elif os.path.isdir(big_path):
            if os.path.islink(big_path):
                sym_dest = os.readlink(big_path)
                echo0('Warning: ln -s "{}" "{}"'
                      ''.format(sym_dest, big_path))
                os.symlink(sym_dest, patch_path)
            else:
                more_added = _diffnames(small_path, big_path, patch_path,
                                        exclude_dotexts=exclude_dotexts)
                if more_added < 1:
                    if os.path.isdir(patch_path):
                        os.rmdir(patch_path)
                files_added += more_added
        else:
            echo0('Error: unknown path type (not link, file, nor dir): "{}"'
                  ''.format(big_path))
    return files_added


def diffnames(small_dir, big_dir, patch_dir, exclude_dotexts=[".pyc"]):
    '''
    Compare two directories and place the added files from the second
    into a third.
    '''
    if not os.path.isdir(small_dir):
        raise FileNotFoundError(small_dir)
    if not os.path.isdir(big_dir):
        raise FileNotFoundError(big_dir)
    _diffnames(small_dir, big_dir, patch_dir, exclude_dotexts=exclude_dotexts)


def main():
    diffnames("C:\\Python32-clean", "C:\\Python32", "C:\\Downloads\\pip+six+dirsync-patch_for_Python3.2")
    return 0


if __name__ == "__main__":
    sys.exit(main())
