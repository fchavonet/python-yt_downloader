#!/usr/bin/env python3

"""
A simple YouTube video downloader.
"""

import customtkinter
import PIL
import pytube


def download():
    """
    Downloads the highest resolution video from a YouTube URL.

    Raises:
        Exception: if there is an error during the download process.
    """
    try:
        url = url_entry.get()
        yt_object = pytube.YouTube(url)
        video = yt_object.streams.get_highest_resolution()
        video.download()
        message_label.configure(text="Download complete!", text_color="green")
    except Exception as e:
        message_label.configure(text=f"{e}", text_color="red")


# Set the appearance mode and default color theme.
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create the main application window.
app = customtkinter.CTk()
app.resizable(False, False)
app.iconbitmap("./yt_downloader_icon.ico")
app.title("YT Downloader")

# Add the logo to the application window.
logo = customtkinter.CTkImage(dark_image=PIL.Image.open("yt_downloader_logo.png"), size=(250, 25))
logo_label = customtkinter.CTkLabel(app, image=logo, text="")
logo_label.pack(padx=0, pady=20)

# Add instructions label.
instructions = customtkinter.CTkLabel(app, text="Paste the YouTube video link you want to download in the field below.")
instructions.pack()

# Add URL entry field.
url_entry = customtkinter.CTkEntry(app, width=600, height=35)
url_entry.pack(padx=20, pady=0)

# Add download button.
download_button = customtkinter.CTkButton(app, text="DOWNLOAD", cursor="hand2", command=download)
download_button.pack(padx=0, pady=20)

# Add message frame for displaying status messages.
message_frame = customtkinter.CTkFrame(app, width=600, height=35)
message_frame.pack_propagate(False)
message_frame.pack(fill="x", padx=20, pady=(0, 20))

# Add message label inside the message frame.
message_label = customtkinter.CTkLabel(message_frame, text="")
message_label.pack(expand=True, fill="both")

# Start the application's main loop.
app.mainloop()
