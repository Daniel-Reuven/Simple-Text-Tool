import sys
from tkinter import *
from tkinter import ttk
from loguru import logger
from functions import encode_base64, decode_base64


def on_click_encode_base64():
    try:
        decoded = input_text_var.get("1.0", END)
        if decoded:
            logger.info(f'Attempting to encode the following string: "{decoded}"'.format())
            final_text = encode_base64(decoded)
            update_interface(final_text, 1)
            logger.info(f'Success:\n"{final_text}"'.format())
        else:
            logger.info(f'Encode Entry text box empty: "{decoded}", nothing to do, skipping.'.format())
    except Exception as e:
        logger.error(f'An Error has occurred: {e}'.format())


def on_click_decode_base64():
    try:
        encoded = input_text_var.get("1.0", END)
        if encoded:
            logger.info(f'Attempting to decode the following string: "{encoded}"'.format())
            final_text = decode_base64(encoded)
            update_interface(final_text, 1)
            logger.info(f'Success:\n"{final_text}"'.format())
        else:
            logger.info(f'Decode Entry text box empty: "{encoded}", nothing to do, skipping.'.format())
    except Exception as e:
        logger.error(f'An Error has occurred: {e}'.format())
        update_interface('Error - Text does not seem to be encoded with Base64 correctly, check log file.', 2)


def update_interface(text, mode):
    if mode == 1:  # Successful action
        output_text_var.configure(state='normal')
        output_text_var.delete('1.0', END)
        output_text_var.insert('end', text)
        output_text_var.configure(state='disabled')
    elif mode == 2:  # Failed action
        output_text_var.configure(state='normal')
        output_text_var.delete('1.0', END)
        output_text_var.insert('end', text)
        output_text_var.configure(state='disabled')


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
    # Label 1 & Entry 1 - Initialize encode section
    encode_var_label = ttk.Label(win, text="Enter Text to ENCODE or DECODE:")
    encode_var_label.pack(fill='both', expand=1)
    input_text_var = Text(win, state='normal', width=65, height=7)
    input_text_var.pack(fill='both', expand=1)
    # Buttons - Initialize buttons section
    btn1 = ttk.Button(win, width=40, text="Encode", command=on_click_encode_base64)
    btn1.pack()
    btn2 = ttk.Button(win, width=40, text="Decode", command=on_click_decode_base64)
    btn2.pack()
    # Label 2 & Output - Initialize Output section
    output_var_label = ttk.Label(win, text="Output:")
    output_var_label.pack(fill='both', expand=1)
    output_text_var = Text(win, state='normal', width=65, height=10)
    # Add a Scrollbar(horizontal)
    v2 = Scrollbar(win, orient='vertical')
    v2.pack(side=RIGHT, fill='y')
    v2.config(command=output_text_var.yview)
    output_text_var.pack(fill='both', expand=1)
    output_text_var.configure(state='disabled')
    # Start the app:
    logger.info(f'Python Text BASE64 Encoder/Decoder has started'.format())
    win.mainloop()
