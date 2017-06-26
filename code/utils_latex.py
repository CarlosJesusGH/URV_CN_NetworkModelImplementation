import settings
import os


def add_image(image_path, caption="", label=""):
    if not os.path.exists(settings.output_latex_path):
        file = open(settings.output_latex_path, 'w+')
        file.write("ini\n")
    else:
        file = open(settings.output_latex_path, 'a')

    image_template = '\t\\begin{figure}[H]\n' \
                     '\t\t\centering\n' \
                     '\t\t\includegraphics[width=1 \\textwidth]{\"/home/cj/Dropbox/Personal/Study/MasterURV/2nd Semester/' \
                     'CN/Activity 1' + image_path.replace('..', '').replace('.png','') + '\"}\n' \
                     '\t\t\caption{' + caption + '}\n' \
                     '\t\t\label{' + label + '}\n' \
                     '\t\end{figure}'
    file.write(image_template + "\n\n")
    file.close()


def add_new_page():
    file = open(settings.output_latex_path, 'a')
    file.write("\n\n%-------------------------------------------------------\n"
               "\\newpage\n")
    file.close()


def add_simple_text(text=""):
    file = open(settings.output_latex_path, 'a')
    file.write(text.replace('_','\\_'))
    file.close()
