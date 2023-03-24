import sys


def ex1():
    numerator = int(input('Type a numerator: '))
    denominator = int(input('Type a denominator: '))

    try:
        res = numerator / denominator
        # raise ZeroDivisionError
        print(f"{numerator} divided into {numerator} is euqal to: {res}")
    except ZeroDivisionError:
        print('Division cannot be performed')
    finally:
        print('Execution fulfilled!!')


def err_ex():
    try:
        """
        This code will arise an exception
        """
        a = 'hi'
        b = int(a)
    except:
        print('Exception caught!')

# ex1()
# err_ex()


def ex2():
    try:
        raise TypeError
    except TypeError:
        print('TypeError Exception caught!')

# ex2()


def ex3():
    try:
        a = int(input('Type the first number: '))
        b = int(input('Type the second number: '))

        if a < 0:
            raise TypeError

        c = a/b
        print("{} / {} = {}".format(a, b, c))
    except ZeroDivisionError:
        print('Division by zero is invalid')
    except ValueError:
        print('Data types are invalid')
    except TypeError:
        print('Value is not in range')

# ex3()


class CustomExcept(Exception):
    def __init__(self):
        super()


def ex4():
    try:
        age = int(input('Type your age: '))
        if age < 18:
            raise CustomExcept
    except ValueError:
        print('Invalid data type')
    except CustomExcept:
        print('Age is less than 18')
    else:
        print('Age is greater than or equal to 18')
    finally:
        print('End')

# ex4()


def ex5():
    class B(Exception):
        pass

    class C(B):
        pass

    class D(C):
        pass

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")


# ex5()


def ex6():
    try:
        f = open('file.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


# ex6()

def ex7():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

# ex7('file.txt')


def ex8():
    raise NameError('Hi')
# ex8()


def ex9():
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise


# ex9()


def exm():
    print(sys.exc_info())

    try:
        raise TypeError
    except:
        print(sys.exc_info())
        try:
            raise ValueError
        except:
            print(sys.exc_info())
        print(sys.exc_info())

    # print(sys.exc_info())

# exm()


def exm1():
    try:
        1/0
    finally:
        return 42

# print('176', 'exm1()', exm1())


def bool_return():
    try:
        return True
    finally:
        return False

# print('184', 'bool_return()', bool_return())


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

# divide(2, 1)
# divide(2, 0)
# divide("2", "1")


def exc_group():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

# exc_group()


# def f():
#     raise ExceptionGroup("group1",
#                          [OSError(1),
#                           SystemError(2),
#                           ExceptionGroup("group2",
#                                          [OSError(3), RecursionError(4)])])


# try:
#     f()
# except* OSError as e:
#     print("There were OSErrors")
# except* SystemError as e:
#     print("There were SystemErrors")

def exm3():
    excs = []
    for test in tests:
        try:
            test.run()
        except Exception as e:
            excs.append(e)

    if excs:
        raise ExceptionGroup("Test Failures", excs)
    
# exm3()

def comment_excp():
    try:
        raise TypeError('bad type')
    except Exception as e:
        e.add_note('Add some information')
        e.add_note('Add some more information')
        raise
comment_excp()

def group_exc():
    def f():
        raise OSError('operation failed')

    excs = []
    for i in range(3):
        try:
            f()
        except Exception as e:
            e.add_note(f'Happened in Iteration {i+1}')
            excs.append(e)

    raise ExceptionGroup('We have some problems', excs)
# group_exc()