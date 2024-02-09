---
title: Variables and Functions
---
## Data types

Unlike Python, variables need to be declared along with their respective types before value assignment in C++. In C++, there are several primitive data types available for use. Underneath it all at the lower levels, the only difference between these primitive data types is their size.

The actual size of data types depends on what compiler we are using. Typical sizes of the primitive data types are as follows:

| Data type | Size (bytes) | Notes |
| ---- | ---- | ---- |
| int | 4 | Signed integer in $(-2^{31}, 2^{31})$. One bit reserved for the sign. |
| short | 2 | Small integers |
| long | at least 4 | Large integers |
| float | 4 | Stores decimals and exponentials |
| double | 8 | Double floating point |
| char | 1 | ASCII value stored in char variables lying in $[0,255]$. |
| bool | 1 | True / False |

> [!hint] 
> The "unsigned" keyword allows us to use the bit occupied by the sign, thus doubling our data range.
> 
> ```cpp
> unsigned int var = 4;
> std::cout << sizeof(var) << std::endl;
> ```
> The "sizeof" operator can be used to check the size allotted by the C++ compiler to the specific data type.

> [!warning] 
> The C++ compiler interprets decimal values as type **double**. To prevent this and force the use of type float, use a suffix "f" or "F" at the end of a float value.
> Note: Unless this is required, better to use double instead of floats to avoid errors when dealing with large numbers.
> ```cpp
> float a = 3.4;  //converted to double
double b = 3E-6;
float c = 4.5F; // forced float

>[!hint]
>The bool data type occupies 1 byte of memory despite being 0 or 1 (represented by one bit). This is on account of addressing memory limitations, as we can only access bytes.


## Functions

Functions in C++ help prevent code duplication. All C++ functions require the declaration to begin with a type and indicate the type of value returned by the function. Type definitions are also required by the function arguments. The function arguments can be either passed _**by value**_ or _**by reference**_.

>[!hint]
>The "main" function is a special case that does not require returning a value.
>The following program in C++ would work without any errors.
>```cpp
>int main(){
>// code here
>// no return statement
>}
>```

### Value
```cpp
int function(int a, int b) {// do something
}

int x=2, y=3, z;
z = function(x, y);
```
When arguments are passed by values, copies of the variables are created and processed by the function without affecting the original variables. In the above example, copies of variables _x_ and _y_ are created when _function_ is called.

### Reference
```cpp
int function(int& a, int& b) {// do something
}

int x=2, y=3, z;
z = function(x, y);
```
With arguments passed by reference, external variables can be accessed directly within the function. in C++, references are indicated with an ampersand (&) sign. In this case, instead of creating a copy, the variable itself is processed by the function. Any modifications made to the local variable are reflected in the variables passed as arguments.


> [!warning]
> As the function with arguments by reference accesses the original variables stored in memory, directly passing values as arguments is not allowed. For example, the following code results in a compilation error.
> ```cpp
> int func(int& a) { std::cout << a << std::endl; }
int main { func(4); }
> ```
> But the following works fine:
> ```cpp
> int func(int& a) { std::cout << a << std::endl; }
int var = 4;
int main { func(var); }
> ```
> Passing values directly without defining variables only works for functions with arguments passed by values due to their variable copying behavior.

**Efficiency considerations** - For functions with arguments passed by values, creating copies of variable types like _int_, _float_, and _char_ is inexpensive. However, creating copies for data types like _string_ can result in a memory overhead. To enable memory-efficient operation, we can replace such functions to use arguments by references with the _const_ keyword.

```cpp
string func(const string& a){
// do something with string a without modifying
}
```
The function above behaves like the arguments by values counterpart, such that the original variables remain unmodified but _without creating copies._
