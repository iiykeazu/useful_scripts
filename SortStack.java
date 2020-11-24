import java.util.Stack;

public class SortStack{
  public Stack<Integer> stack;
  public SortStack(Stack<Integer> stack1){
    stack = stack1;
    Stack<Integer> aux = new Stack<Integer>();
    while (!stack.empty()){
      if (aux.empty() || stack.peek() <= aux.peek()){
        aux.push(stack.pop());
      } else if(stack.peek()>aux.peek()){
        int store = stack.pop();
        while (!aux.empty() && store > aux.peek()){
          stack.push(aux.pop());
        }
        aux.push(store);
      }
    }
    stack = aux;
  }
  public Stack getStack(){
    return stack;
  }
}
