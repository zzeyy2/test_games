import asyncio
from core.database.db import *
from core.utils import is_digit_or_none
import os


async def manager(db: GameDB):

    #Комментариев не добавил, никто мой код кроме тебя читать не будет)

    print("\n1. Добавить игру")
    print("2. Найти игру")
    print("3. Удалить игру")
    print("4. Обновить игру")
    print("5. Просмотреть все игры")

    choice = input(f'Что вы хотите сделать?:\n')


    if '1' in choice:

        title=input(f'Введите название игры:\n')
        publisher=input(f'Введите издателя игры:\n')
        year=is_digit_or_none(input(f'Введите год издания игры:\n'))

        os.system('cls||clear')

        if not any((title, publisher, year)):
            print('Вы не ввели никаких данных!')
            return
        
        if await db.add(title, publisher, year):
            print('Данные успешно добавлены!')

        else:
            print('Игра уже добавлена!')

        

    elif '2' in choice:
        print(f'Если хотите пропустить шаг - оставьте поле пустым')

        title=input(f'Введите название игры:\n')
        publisher=input(f'Введите издателя игры:\n')
        year=is_digit_or_none(input(f'Введите год издания игры:\n'))


        os.system('cls||clear')

        if not any((title, publisher, year)):
            print('Вы не ввели никаких данных!')
            return
        
        games = await db.search(title, publisher, year)

        if games:
            print(f'Название|Издатель|Год')

            for game in games:
                game = [str(_) for _ in game]

                print('|'.join(game))
        else:
            print('Игра не найдена!')

        


    elif '3' in choice:
        print(f'Если хотите пропустить шаг - оставьте поле пустым')

        title=input(f'Введите название игры:\n')
        publisher=input(f'Введите издателя игры:\n')
        year=is_digit_or_none(input(f'Введите год издания игры:\n'))
        
        os.system('cls||clear')

        if not any((title, publisher, year)):
            print('Вы не ввели никаких данных!')
            return
        
        if await db.remove(title, publisher, year):
            print('Игра успешно удалена!')
        else:
            print('Игра не найдена!')

        
            

    elif '4' in choice:
        print(f'Если хотите пропустить шаг - оставьте поле пустым')

        old_title=input(f'Введите старое название игры:\n')
        old_publisher=input(f'Введите старого издателя игры:\n')
        old_year=is_digit_or_none(input(f'Введите старый год издания игры:\n'))

        if not any((old_title, old_publisher, old_year)):
            os.system('cls||clear')
            print('Вы не ввели данных необходимых для поиска\nПопробуйте еще раз')
            return
        
        if not await db.search(old_title, old_publisher, old_year):
            os.system('cls||clear')
            print('Игра не найдена!')
            return
        

        new_title=input(f'Введите новое название игры:\n')
        new_publisher=input(f'Введите нового издателя игры:\n')
        new_year=is_digit_or_none(input(f'Введите новый год издания игры:\n'))

        os.system('cls||clear')

        if not any((new_title, new_publisher, new_year)):
            print('Вы не ввели данных необходимых для обновления текущих\nДанные игры остались прежними')
            return


        
        if await db.edit(old_title, old_publisher, old_year, new_title, new_publisher, new_year):
            print('Успешно изменены данные игры!')
        else:
            print('Игра не найдена!')
        

    elif '5' in choice:
        games = await db.get_all()

        if not games:
            os.system('cls||clear')
            print("База данных пустая. Вам нужно добавить игры,\nчто бы пользоваться этой функцией")
            return
        
        os.system('cls||clear')
        print(f'Название|Издатель|Год')
        for game in games:
            game = [str(_) for _ in game]
                
            print('|'.join(game))


            

async def main():
    db = GameDB(r'core/database/db.db')
    await db._initialize()

    while True:
        await asyncio.create_task(manager(
            db=db
        ))
        
            





if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
