import java.util.ArrayList;
import java.util.EmptyStackException;
class Node{
  public Node above, below;
  public int value;
  public Node(int value){
    this.value = value;
  }
}
public class SetOfStacks{
  private ArrayList<Stack> stacks = new ArrayList<Stack>();
  private int capacity;
  public SetOfStacks(int capacity){
    this.capacity = capacity;
  }

  public Stack getLastStack(){
    if (stacks.size() == 0) return null;
    return stacks.get(stacks.size()-1);
  }

  public void push(int value){
    Stack last = getLastStack();
    if (last != null && !last.isFull()){
      last.push(value);
    } else {
      Stack stack =  new Stack(capacity);
      stack.push(value);
      stacks.add(stack);
    }
  }
  public int pop(){
    Stack last = getLastStack();
    if (last == null){
      throw new EmptyStackException();
    }
    int value = last.pop();
    if (last.size == 0) stacks.remove(stacks.size()-1);
    return value;
  }

  public boolean isEmpty(){
    Stack last = getLastStack();
    return last == null || last.isEmpty();
  }

  public int popAt(int index){
    if (index < 0 || index > stacks.size()) throw new IndexOutOfBoundsException();
    return leftShift(index, true);
  }

  public int leftShift(int index, boolean removeTop){
    Stack stack = stacks.get(index);
    int removed_item;
    if (removeTop) removed_item = stack.pop();
    else removed_item = stack.removeBottom();
    if (stacks.get(index).isEmpty()){
      stacks.remove(index);
    } else if (index + 1 < stacks.size()){
      int value = leftShift(index+1, false);
      stack.push(value);
    }
    return removed_item;
  }
}
class Stack{
  private int capacity;
  public Node top, bottom;
  public int size = 0;

  public Stack(int capacity){
    this.capacity = capacity;
  }
  public boolean isFull(){ return capacity == size;}
  public boolean isEmpty(){ return size == 0;}

  public void join(Node above, Node below){
    if (below != null) below.above = above;
    if (above != null) above.below = below;
  }
  public boolean push(int value){
    Node n = new Node(value);
    if (size < capacity){
      join(n,top);
      top = n;
      if (size == 1) bottom = n;
      size ++;
      return true;
    } else {
      return false;
    }
  }

  public int pop(){
    if (size == 0) throw new EmptyStackException();
    Node t = top;
    top = top.below;
    if (top != null) top.above = null;
    if (top == null) bottom = null;
    size --;
    return t.value;
  }

  public int removeBottom(){
    Node b = bottom;
    bottom = bottom.above;
    if (bottom != null) bottom.below = null;
    size --;
    return b.value;
  }
}
