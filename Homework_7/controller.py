import model
import view

def click ():
    regime =int(view.choose_regime())
    if regime == 1:
        view.print_data(model.exp())
    elif regime == 2:
        view.print_data(model.imp())
    else:
        print("Выберите режим 1 или 2")