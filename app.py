from view import show_collection, show_message
from core import create_task, deleted_task, edit_task
from utils import check_confirm
from storage import save_collection, load_collection


"""основной цикл"""


def app():
    name_file = os.path.join("saves.txt")
    collection = load_collection(task_list[], name_file)
    is_running = True

    while is_running:
        print('1 = посмиотреть задачи'
              '\n2 - добавить задачу'
              '\n3 - редактирование'
              '\n4 - снять задачу'
              '\n5 - выход')
        choice_user