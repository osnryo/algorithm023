// 用 add first 或 add last 这套新的 API 改写 Deque 的代码
// Java代码

Deque<String> deque = new LinkedList<String>();
deque.addLast("a");
deque.addLast("b");
deque.addLast("c");
System.out.println(deque);

String str = deque.peek();
System.out.println(str);
System.out.println(deque);

while(deque.size()>0){
    System.out.println(deque.pop());
}
System.out.println(deque);