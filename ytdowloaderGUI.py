import dearpygui.dearpygui as dpg
import YtAudio0

dpg.create_context()


def change_text(sender, app_data):
    dpg.set_item_label("download", "Downloading...")
    print("downloading")
    download(app_data)


def download(app_data):
    print(app_data['file_path_name'])
    download_path = app_data['file_path_name']
    YtAudio0.download_video(dpg.get_value("input_text"), download_path)
    
    dpg.set_item_label("download", "Download Complete")



def main():
        
    with dpg.item_handler_registry(tag="handler thingy") as handler:
        dpg.add_item_clicked_handler(callback = change_text)
#        dpg.add_item_clicked_handler(callback = download)
    dpg.add_file_dialog(directory_selector=True, show=False, tag="file_dialog_id", callback=change_text)


    with dpg.window(tag="fsdjf"):
        dpg.add_text("Enter the URL of the video you want to download")
        dpg.add_input_text(tag="input_text",label="URL or Song Name and Artist Name", width=500, height=25)
        dpg.add_button(tag="download", label="Download", width=500, height=25,callback=lambda: dpg.show_item("file_dialog_id"))


#    dpg.bind_item_handler_registry("download","handler thingy")

    dpg.create_viewport(title="Youtube Downloader", width=750, height=300)


    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("fsdjf", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()