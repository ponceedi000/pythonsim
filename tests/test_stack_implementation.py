from pythonism.stack_iterator import Stack
import pytest

#TEST ONE - Can successfully push onto a stack
def test_stack_push():
    stack = Stack()
    stack.push(1)
    actual = stack.top.value
    expected = 1
    assert actual == expected

# TEST TWO - Can successfully push multiple values onto a stack
def test_stack_push_multiple_values():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.top.value
    expected = 3
    assert actual == expected

# TEST THREE - Can successfully pop off the stack
def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    actual = stack.top.value
    expected = 2
    assert actual == expected

# TEST FOUR - Can successfully empty a stack after multiple pops
def test_stack_multiple_pops():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.pop()
    expected = Exception
    assert actual == expected

# TEST FIVE - Can successfully peek the next item on the stack
def test_stack_peek():
    stack = Stack()
    stack.push(3)
    actual = stack.peek()
    expected = 3
    assert actual == expected

# TEST SIX - Can successfully instantiate an empty stack
def test_stack_is_empty_True():
    stack = Stack()
    assert stack.is_empty() == True

# TEST SEVEN - Calling pop on empty stack raises exception
def test_stack_empty_pop_raise_exception():
    stack = Stack()
    actual = stack.pop()
    expected = Exception
    assert actual == expected

    # <--- AND --->

# TEST SEVEN (cont'd) - Calling peek on empty stack raises exception
def test_stack_empty_peek_raise_exception():
    with pytest.raises(Exception):
        stack = Stack()
        stack.peek()