'''
Розробити приклад використанням реалізації
абстрактного типу даних
'''

class Super:
    def action(self):
        raise NotImplementedError('action must be defined')

class Sub(Super):
     def action(self):
         print('in Sub.action')
    #pass
if __name__ == "__main__":
    x = Sub()
    x.action()