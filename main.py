import asyncio
from core.database.db import *
from core.utils import is_digit_or_none
import os
from contextlib import suppress



async def main():
    db = GameDB(r'core/database/db.db')
    await db.initialize()

    while True:
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
            await db.add(title, publisher, year)
            

        elif '2' in choice:
            print(f'Если хотите пропустить шаг - оставьте поле пустым')

            title=input(f'Введите название игры:\n')
            publisher=input(f'Введите издателя игры:\n')
            year=is_digit_or_none(input(f'Введите год издания игры:\n'))
            
            os.system('cls||clear')
            games = await db.search(title, publisher, year)
            

            print(f'Название|Издатель|Год')

            for game in games:
                game = [str(_) for _ in game]

                print('|'.join(game))
            
        elif '3' in choice:
            print(f'Если хотите пропустить шаг - оставьте поле пустым')

            title=input(f'Введите название игры:\n')
            publisher=input(f'Введите издателя игры:\n')
            year=is_digit_or_none(input(f'Введите год издания игры:\n'))
            
            os.system('cls||clear')
            games = await db.remove(title, publisher, year)
            
        elif '4' in choice:
            print(f'Если хотите пропустить шаг - оставьте поле пустым')

            old_title=input(f'Введите старое название игры:\n')
            old_publisher=input(f'Введите старого издателя игры:\n')
            old_year=is_digit_or_none(input(f'Введите старый год издания игры:\n'))
            
            new_title=input(f'Введите новое название игры:\n')
            new_publisher=input(f'Введите нового издателя игры:\n')
            new_year=is_digit_or_none(input(f'Введите новый год издания игры:\n'))
            


            os.system('cls||clear')
            games = await db.edit(old_title, old_publisher, old_year, new_title, new_publisher, new_year)
        elif '5' in choice:
            games = await db.get_all()
            

            print(f'Название|Издатель|Год')
            for game in games:
                game = [str(_) for _ in game]
                
                        
                print('|'.join(game))





if __name__ == "__main__":
    asyncio.run(main())
