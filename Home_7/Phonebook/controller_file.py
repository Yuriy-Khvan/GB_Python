import data_generator, view_file, export_file, import_file

data_generator.user_generate()

def button():
    mode = view_file.choose()
    if mode == '+':
        import_file.import_fun(view_file.for_import())
    else:
        view_file.print_export(export_file.export_fun(view_file.for_export))

button()