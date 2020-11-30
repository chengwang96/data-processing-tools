error_code_dict = {
    0: 'success',
    1: 'file not found',
    2: 'file type error'
}


def check_error_code(error_code):
    if error_code != 0:
        print(error_code_dict[error_code])
        exit()