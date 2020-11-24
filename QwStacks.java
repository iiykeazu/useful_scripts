import java.util.Stack;
import java.util.EmptyStackException;

public class QwStacks <T>{
  private Stack <T> stackA, stackB;
  public QwStacks(){
    stackA = new Stack <T>();
    stackB = new Stack <T>();
  }

  public void AtoB(){
    while (!stackA.empty()){
      stackB.push(stackA.pop());
    }
  }

  public void add(T item){
    stackA.push(item);
  }

  public T remove(){
    if (isEmpty()){
      throw new EmptyStackException();
    }
    if(stackB.empty()){
      AtoB();
    }
    return stackB.pop();
  }
  public T peek(){
    if (stackB.empty()){
      AtoB();
    }
    return stackB.peek();
  }

  public boolean isEmpty(){
    return stackA.empty() && stackB.empty();
  }
}
