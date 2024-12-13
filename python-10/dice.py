import tkinter
import random

def rolldice():
    result = random.randint(1, 6)
    dice_image = dice_images[result - 1]
    label.config(image=dice_image)
    label.image = dice_image

def main():
    global label, dice_images
    root = tkinter.Tk()
    root.geometry("300x300")
    root.title("Dice Roller")

    try:
        dice_images = [
            tkinter.PhotoImage(file="assets/dice-1.png").subsample(3, 3),
            tkinter.PhotoImage(file="assets/dice-2.png").subsample(3, 3),
            tkinter.PhotoImage(file="assets/dice-3.png").subsample(3, 3),
            tkinter.PhotoImage(file="assets/dice-4.png").subsample(3, 3),
            tkinter.PhotoImage(file="assets/dice-5.png").subsample(3, 3),
            tkinter.PhotoImage(file="assets/dice-6.png").subsample(3, 3)
        ]
    except tkinter.TclError as e:
        print(f"Error loading images: {e}")
        root.destroy()
        return

    label = tkinter.Label(root)
    label.pack(expand=True)
    button = tkinter.Button(root, text="Roll", command=rolldice)
    button.pack(expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
