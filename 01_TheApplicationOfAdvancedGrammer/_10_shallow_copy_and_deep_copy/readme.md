- 深拷贝和浅拷贝对可变对象和不可变对象的影响不是不一样的

- 可变对象：列表，集合，字典

  - 浅拷贝关系中，只有最顶层的对象元素被拷贝，而子对象元素没有被拷贝，是原来的那一份

  - 深拷贝关系中，所有层级的对象元素都是新的对象，完全独立于原来的数据

    ![image-20251030214434821](C:\Users\keeplooking\PycharmProjects\RediscoveringTheJoyOfProgramming\01_TheApplicationOfAdvancedGrammer\_10_shallow_copy_and_deep_copy\image-20251030214434821.png)

- 不可变对象：数字，字符串，元组

  - 拷贝无意义，拷贝的目的是确保两份数据不会冲突，而不可变对象是在初始化之后就无法改变了
  - 特殊情况：不可变对象中包含了可变对象，该数据在深拷贝关系中，是完全独立于原来的数据，在浅拷贝关系中都是用的原来的同一个对象
  - ![image-20251030214307910](C:\Users\keeplooking\PycharmProjects\RediscoveringTheJoyOfProgramming\01_TheApplicationOfAdvancedGrammer\_10_shallow_copy_and_deep_copy\image-20251030214307910.png)

  