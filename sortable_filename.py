
def sortable_filename(filestr, fileext):

    from datetime import datetime

    return filestr + datetime.now().strftime("%Y%m%d%H%M%S") + '.' + fileext