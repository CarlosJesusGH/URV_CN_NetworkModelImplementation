import os, sys
import pyperclip

directory = "../../output/plots/barabasi_albert/"
template = ""

# Go over all files ordered by name
for filename in sorted(os.listdir(directory)):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        isEndOfPage = False
        print "Adding image: " + filename
        filename = filename.replace(".png", "")
        filename = filename.replace(".jpg", "")
        complete_filename = filename
        caption = filename
        caption = caption.replace("_","\_")
        # filename = filename[filename.index('_') + 1:]
        if caption.endswith("\_deg\_dist"):
            caption = "Degree distribution"
            isEndOfPage = True
        # Concatenate template
        template = template + caption + "\n\n"
        template = template + "\\begin{figure}[H]\n\
  \centering\n\
  \includegraphics[width=0.8 \\textwidth]{{{\"" + directory + complete_filename + "\"}}}\n\
  \caption{" + caption + "}\n\
\end{figure}\n\n\n"
        if isEndOfPage:
            template = template + "\\newpage\n\n\n"
        continue
    else:
        continue

# Copy template to clipboard
pyperclip.copy(template)
# print pyperclip.paste()
print "output created and copied to clipboard (Just paste text using Ctrl+V)"
