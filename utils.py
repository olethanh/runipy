import os
from StringIO import StringIO

from IPython.core.display import HTML, display

def get_base_export_path():
    ip = get_ipython()
    if ip.config.Railnova.get('export_path'):
            path = ip.config.Railnova.get('export_path')
    elif 'NB_FILES_EXPORT_PATH' in os.environ:
            path = os.environ['NB_FILES_EXPORT_PATH']
    else:
            path = os.getcwd()
    return path

def get_base_export_url():
    ip = get_ipython()
    if ip.config.Railnova.get('base_url'):
            path = ip.config.Railnova.get('base_url')
    elif 'NB_FILES_EXPORT_URL' in os.environ:
            path = os.environ['NB_FILES_EXPORT_URL']
    else:
        path = 'file://' + get_base_export_path()
    print path
    return path

def fn_for_export(name):
    if "/" in name:
        raise Exception("You aren't able to put a '/' in the filename")

    if not isinstance(name, basestring):
        raise Exception("The file name should be a string")


    return os.path.join(get_base_export_path(), name)


def export(name, content):
    if not isinstance(content, basestring):
        raise Exception("The file content should be a string")

    open(fn_for_export(name), "w").write(content)


def output(name):
    fn = fn_for_export(name)
    if not fn:
        return StringIO()

    return open(fn, "wb")

def url_for_report(name):
    base_url = get_base_export_url()
    return "%s/%s" % (base_url, name)

def link_for_report(name):
    url = url_for_report(name)
    return display(HTML('<a href="%s">Download %s</a>' % (url, name)))


def load_vega():
    display(HTML('''<script>$.getScript("https://public.railnova.eu/d3.min.js", function() {
                setTimeout(function () { 

                $.getScript("https://public.railnova.eu/vega.min.js", function() {
                    })
                    }, 5)
            });</script>'''
    ))

def export_csv(dataframe, csv_file_name):
    file_name = csv_file_name + ".csv"
    file_output = output(file_name)
    dataframe.to_csv(file_output, sep=';', float_format='%.3f')
    print file_name
    return  file_name

def export_excel(dataframe, excel_file_name, **kwargs):
    file_name = excel_file_name + ".xls"
    file_output = output(file_name)
    dataframe.to_excel(file_output, float_format='%.3f', **kwargs)
    print file_name
    return  file_name

