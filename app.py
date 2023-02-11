import sys
from tkinter import *
from tkinter import ttk
from loguru import logger
from functions import encode_base64, decode_base64


def on_click_encode_base64():
    try:
        decoded = encode_var_entry.get()
        if decoded:
            logger.info(f'Attempting to encode the following string: "{decoded}"'.format())
            final_text = encode_base64(decoded)
            update_interface(final_text, 1)
            logger.info(f'Success: "{final_text}"'.format())
        else:
            logger.info(f'Encode Entry text box empty: "{decoded}", nothing to do, skipping.'.format())
    except Exception as e:
        logger.error(f'An Error has occurred: {e}'.format())


def on_click_decode_base64():
    try:
        encoded = decode_var_entry.get()
        if encoded:
            logger.info(f'Attempting to decode the following string: "{encoded}"'.format())
            final_text = decode_base64(encoded)
            update_interface(final_text, 1)
            logger.info(f'Success: "{final_text}"'.format())
        else:
            logger.info(f'Decode Entry text box empty: "{encoded}", nothing to do, skipping.'.format())
    except Exception as e:
        logger.error(f'An Error has occurred: {e}'.format())
        update_interface('Error - Text does not seem to be encoded with Base64 correctly, check log file.', 2)


def update_interface(text, mode):
    if mode == 1:  # Successful action
        output_var_entry.config(state='normal')
        output_var_entry.delete(0, 'end')
        output_var_entry.insert(0, text)
        output_var_entry.config(state='readonly')
    elif mode == 2:  # Failed action
        output_var_entry.config(state='normal')
        output_var_entry.delete(0, 'end')
        output_var_entry.insert(0, text)
        output_var_entry.config(state='readonly')


if __name__ == '__main__':
    logger.add("App_Log_{time}.log", rotation="30 days", backtrace=True, enqueue=False, catch=True)
    if sys.version_info < (3, 7):
        raise Exception("Must be using Python 3.7 and above")
    # Initialize Tkinter:
    win = Tk()
    win.title("Python Text BASE64 Encoder/Decoder")
    win.geometry("500x400")
    win.minsize(500, 400)
    win.maxsize(500, 400)
    frame = ttk.LabelFrame(win, width=500)
    frame.pack(padx=10, pady=10)
    frame2 = ttk.LabelFrame(win, width=500)
    frame2.grid_rowconfigure(0, weight=1)
    frame2.grid_columnconfigure(0, weight=1)
    frame2.pack(padx=10, pady=10, fill='both', side='bottom', expand='true')
    # Label 1 & Entry 1 - Initialize encode section
    encode_var_label = ttk.Label(frame, text="Enter Text to ENCODE:")
    encode_var_label.grid(row=0, column=0, sticky=W)
    encode_var_entry = ttk.Entry(frame, width=65)
    encode_var_entry.grid(row=1, columnspan=4, padx=2, pady=3)
    # Label 2 & Entry 2 - Initialize decode section
    decode_var_label = ttk.Label(frame, text="Enter Text to DECODE:")
    decode_var_label.grid(row=2, column=0, sticky=W)
    decode_var_entry = ttk.Entry(frame, width=65)
    decode_var_entry.grid(row=3, columnspan=4, padx=2, pady=3)
    # Label 3 & Output 3 - Initialize Output section

    frm_container = ttk.Frame(frame2)
    frm_container.grid(row=0, column=0, sticky=NSEW)
    frm_container.columnconfigure(0, weight=1)
    frm_container.columnconfigure(0, weight=100)
    frm_container.rowconfigure(1, weight=1)
    output_var_label = ttk.Label(frm_container, text="Output:")
    output_var_label.grid(row=0, column=0, sticky=W)
    output_var_entry = ttk.Entry(frm_container, state='readonly')
    output_var_entry.grid(row=1, column=0, sticky=NSEW)
    # Buttons - Initialize buttons section
    btn1 = ttk.Button(frame, width=15, text="Encode", command=on_click_encode_base64)
    btn1.grid(row=4, column=0, columnspan=2, padx=20, pady=5, sticky=W)
    btn2 = ttk.Button(frame, width=15, text="Decode", command=on_click_decode_base64)
    btn2.grid(row=4, column=2, columnspan=2, padx=20, pady=5, sticky=W)
    # Start the app:
    logger.info(f'Python Text BASE64 Encoder/Decoder has started'.format())
    win.mainloop()
