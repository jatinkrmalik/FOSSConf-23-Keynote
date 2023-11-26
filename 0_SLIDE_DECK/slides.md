%title: #FOSSConf23
%author: @jatinkrmalik
%date: 2023-11-26

-> # Elevate Your Code: Practical Insights for 10X Impact <-




-> > Jatin K Malik <-

---

# Quick intro about me:

`0_SLIDE_DECK/intro_jatin.png`

^

`0_SLIDE_DECK/hobbies_jatin.png`

---

I really appreciate what you folks at **FOSSCU** are trying to do! 
^

One of the best ways to set yourself apart from the crowd is to **contribute to open source**. 

---

Welcome to a session where we will try to **elevate our coding** skills together!
^

This is going to be mostly hands-on code. I assume most of us here are **developers**, so I will try to keep it as **technical** as possible. 
^

> Language of choice is **Python**, but the concepts are language agnostic! 
^

> Feel free to interrupt me and ask question, but I may chose to park them for later, if we are running out of time.

---

# Agenda:

1. **Mastering Code Craftsmanship**

2. **Principles of Effective Coding**

3. **The Balancing Act**

4. **Coding Paradigms in Focus**

5. **Wisdom Beyond the Code**

6. **Q/A**
   

---

Let's dive in!

---

There is a very popular _quote_:

---

> "There are only two hard things in Computer Science:
^
>
> 1. Cache invalidation
> 
^
>
> 2. Naming things!"
> 
^
>
>> - Phil Karlton

---

It's only natural we address **Naming Things in Code** first! 

---

These are the **common pitfalls** I see in the code often while reviewing:

---

`1_naming_things/0_bad_code.py`

It seems to be failing a test case! Let's try to **debug** it? 

---

Worst thing you can do to fix this is: 

`1_naming_things/1_still_bad_code.py`

We will talk more about this! 

---

In this `1_naming_things/2_good_code.py` version, each point is addressed:

- **Avoid Single Letter Variable Names:**  Used descriptive names like `product`, `order`.
^

- **Don't Abbreviate Names:** Avoided abbreviations like `pr`, used `price`, `name`.
^

- **Avoid Putting Types in Names:** Removed type indications from variable names.
^

- **Include Units in Variable Names:** Specified units in names like `tax_rate`.
^

- **Be Cautious with Naming Conventions:** Used clear class names without unnecessary prefixes.
^

- **Rethink Naming if Struggling:** Renamed `util_calc` to `calculate_order_total` for clarity.
^

- **Organize Code Logically:**  Organized functions and classes logically with clear responsibilities.

---

Remember, I said we will talk more about `1_naming_things/1_still_bad_code.py` and why those comments are bad?

^

Let me take you on a stroll on how to **NOT** comment!

---

But first, tell me **what's wrong** with this code?

`2_comments/0_bad_code.py`

---

In this `2_comments/1_stll_good_code.py` version, each point is addressed:

- **Avoiding Comments in Code:** 
  - Removed comments that explain what the code is doing, as the code itself is clear enough.
^
- **Use of Constants:** 
  - Introduced constants like `OLD_BOOK_YEAR_THRESHOLD` to replace unclear numeric literals.
^
- **Refactoring Complex Code:** 
  - Broke down complex logic into simpler parts with clear variable names for better readability.
^
- **Function Extraction:** 
  - Moved complex logic into functions like `is_eligible_for_discount` for better organization and readability.

...

---

- **Leveraging Types:** 
  - Added type hints and used descriptive variable names to make the code more understandable.
^
- **Problems with Comments:** 
  - Ensured that the code is straightforward enough to not require comments that could become outdated or misleading.
^
- **Documentation vs. Comments:** 
  - Emphasized writing clear code over using comments to explain internal workings.
^
- **Valid Use Cases for Comments:** 
  - Included comments to explain the purpose of constants, which is a valid use of comments.
^
- **Code as a Specification:** 
  - Ensured that the code itself clearly specifies what it does, reducing the need for additional explanation.


---

Look how clean the code looks now!

`2_comments/2_good_code.py`

---

Now, let's shift gears! 

^

You know what grind my gears while reviewing code? 

^

Nesting!
^
# LOADS OF NESTING! 

---

Let's see an example of this:

`3_nesting_syndrome/0_bad_code.py`

---

In the `3_nesting_syndrome/1_better_code.py` version, we addressed:

- We use early returns to handle each validation check, which helps to avoid deep nesting.
^

- All logic is kept within the process_user_data function offering a simpler refactoring step that still significantly improves readability and maintainability.

---

But now, let's look at `3_nesting_syndrome/2_good_code.py` version, where we addressed:

- We use a separate function `validate_user_data` to handle validations, reducing the depth of nesting.
^

- We apply the principle of early returns (inversion) to handle error conditions upfront.
^

- The `process_user_data` function becomes more focused and easier to understand, handling only the core processing logic.

---

But, what is one of the most "overused" and "popular" set of principles in programming? 

^
Any guesses! 

^
Yep! You guessed it right!

---

-> # S.O.L.I.D. <-

^ 
Let's see what it stands for:
^
- **S** ingle Responsibility Principle
^
- **O** pen/Closed Principle
^
- **L** iskov Substitution Principle
^
- **I** nterface Segregation Principle
^
- **D** ependency Inversion Principle

---

I am not here to bore you with theory, so let's see **some hands on code**! 

So, looking into `4_solid/0_bad_code.py` what do you see? 

---

What can be better? Let's see: 

`4_solid/1_better_code.py`

---

What did we change to make it better?
^

- **Separation of Concerns:** The `PaymentProcessor` and `DeliveryService` classes are introduced to handle payment and delivery, respectively, separating these concerns from the `BookStore` class.
^

- **Some Abstraction:** While not fully abstract or extensible, the `PaymentProcessor` and `DeliveryService` provide a layer of abstraction, making it easier to modify payment and delivery logic independently.
^  

- **Simplified BookStore Class:** The `BookStore` class is now more focused on managing books, with less responsibility for payment and delivery.


---

But what's absolutely the best way to write it? 

`4_solid/2_good_code.py`

---

# What did we change to write the absolute best code? 
^

- **Single Responsibility Principle (SRP):** Each class (`Book`, `BookRepository`, `PaymentProcessor`, etc.) has a single responsibility.
^

- **Open/Closed Principle (OCP):** `PaymentProcessor` and `DeliveryService` are designed to be extended without modifying existing code.
^

- **Liskov Substitution Principle (LSP):** `OnlineBookStore` can use any subclass of `PaymentProcessor` and `DeliveryService` without knowing the specific type.
^

- **Interface Segregation Principle (ISP):** Specific interfaces ( `PaymentProcessor`, `DeliveryService` ) are created, ensuring that classes don't depend on interfaces they don't use.
^

- **Dependency Inversion Principle (DIP):** `OnlineBookStore` depends on abstractions ( `BookRepository`, `PaymentProcessor`, `DeliveryService` ) rather than concrete implementations.


---

# Now comes the ultimate question? 

^

Is "good" code always **good**? Or is it more of a **ideal** code? 

^

Can we say **better code** is actually **good enough**?

---

# Premature Optimization 

This is one of my **favorite topics** to talk about internally at work as well! 
^

I even published an internal blog on same topic. _I may publish it externally soon!_

---

-> # Y.A.G.N.I. <-

^

-> You Ain't Gonna Need It! <-

---

# Premature Optimization 

Often discussions about performance optimization are premature and can distract from more important aspects of development! 

Performance should be balanced with velocity (speed of adding new features) and adaptability (ease of changing the system to new requirements).

---

You should think of any project in the following scale: 

- 0 -> 1 
- 1 -> 10 
- 10 -> 100
- ... 

---

There is a funny joke about this in Webdev community:
^

> "If your website has a favicon, you have shipped too late!"

---

-> **Facebook** also comes to my mind! <-

The initial use of PHP for Facebook, despite its inefficiencies and criticism, was beneficial for rapid development.
Performance issues were addressed later as they became significant.

^ 
And we saw a lot of open source tech that came out of Facebook ahem...Meta! 
^

-> **React, GraphQL, PyTorch, Cassandra** to name a few! <- 

---

Let's look at some code: 

`5_yagni/0_premature.py` is a perfect example of what not to do from the start, unless it's well documented and a part of your spec.

---

`5_yagni/1_kiss.py` is a good example of how to write code that is good enough and can be optimized later if needed.

---

> I often see candidates an interview forgetting the original scope of the question and then go on to make something super complex! 
^

> The database incident(popular language q) is a perfect example of this!

---

Let's see some more examples on how **minor optimizations** can be _insignificant_ in the broader context of application performance! 

---

`5_yagni/2_optimized.py` 

> a set is used to find unique numbers in a list. While using a set is _efficient_ for this purpose, if the primary goal is readability or the list is not large enough to warrant optimization, this approach might be **overkill**.

---

`5_yagni/3_balanced.py` 

> the function is simplified by directly converting the list to a set and back to a list. This approach is more **readable** and still **maintains efficiency** for most practical purposes.

---

> The key takeaway is that while _optimizations can be beneficial_, they should be applied **judiciously** and **in context**. 
>
> Over-optimizing can lead to code that is **harder to read and maintain** without providing _significant performance benefits_.

---

# W.E.T v/s D.R.Y

> Similar story here! You folks know the full form, right? 

^

- **WET**: Write Everything Twice
- **DRY**: Don't Repeat Yourself

---

Let's look at some code: 

`6_dry_or_wet/0_dry.py` 

What do you think? 

---

And, here's another one: 

`6_dry_or_wet/1_wet.py`

---

Which one is a better approach? 

^

# It depends!

---

# DRY

- **Reduces Redundancy**   
- **Improves Maintainability**
- **Avoids Bugs** 

^

# WET

- **Simplicity in Early Stages** 
- **Avoids Premature Abstraction** 
- **Learning and Experimentation** 

---

> In practice, a **balance** between DRY and WET principles is often the best approach. Over-applying DRY can lead to **premature abstraction**, while too much WET can lead to a codebase that's **hard to maintain** and update.

---

# Time check! 

---

I wanted to touch a bit on my another favorite topic:

# Asynchronous vs. Synchronous Programming

---

-> Can anyone explain me what's the difference? <- 

---

Let's see a demo! 

**Sync**: `7_async_vs_sync/0_sync.py`

^

**Async**: `7_async_vs_sync/1_async.py`

---

-> But isn't Python **Single Threaded** as GIL limits it? <-

^


-> Well, the answers is in your Kitchen! Hear me out! <-

--- 

Now who can tell me the difference b/w **Multi-Threading** & **Multi-Processing**?

---

It's very crucial to know the key underlying hardware concepts as when you grow ranks in your SWE journey, these things start to matter a lot!

Your job evolves from writing code to **designing scalable systems**!

---

-> **Paging** <-
^
-> **Virtual Memory** <-
^
-> **Cache** (L1 vs L2) <-
^
-> **Disk I/O** <-
^
-> **IPC (Inter-Process Communication)** <-
^
-> **Networking** (OSI model?) <-

---

# Outro

Who is a **Principal Engineer** btw? 

^

0_SLIDE_DECK/principal_engineer.gif


---

# In all seriousness: 

- **Delayed** gratification! 
^

- Context switching to **101%**.
^

- Coding is **no longer** a priority, but I still (try to) code. 
^

- **Meetings** galore! 
^

- Becoming comfortable with **uncertainty**.

---

-> Q/A <-

-> Go on! Ask me some spicy questions? <- 

---

-> # Thank You! <-




-> █▀▀▀▀▀█  ▄▄▀▀▄█ ▄ █▀▀▀▀▀█  <-
-> █ ███ █ ▄   █▄ █▄ █ ███ █  <-
-> █ ▀▀▀ █ ▀▀ ▄▄█  ▀ █ ▀▀▀ █  <-
-> ▀▀▀▀▀▀▀ ▀ █▄▀ █ █ ▀▀▀▀▀▀▀  <-
-> █▀▄ ▄█▀▀ █ ▀▄▀▀█▀  ▄██▄▄   <-
-> ▀▄███▀▀█▀▄▀ ▄▀ ▀▀▄▀▄██ ▀█  <-
-> █▄▄█▄▀▀ ▀▀ ▀▀▄ ██ ▀▀   ▄▀  <-
-> █  █▀▀▀▀  ▄█▀ ▀█▄█   ▀▄▀█  <-
-> ▀ ▀▀ ▀▀▀█▀█▀█▀▀ █▀▀▀█ █    <-
-> █▀▀▀▀▀█ █▀ █▄▀█▄█ ▀ █▀ ▄█  <-
-> █ ███ █  █ █▀███▀███▀█▀▄▄  <-
-> █ ▀▀▀ █ ▄▀█ ▄ ▀ █▄ █▄ ▀ █  <-
-> ▀▀▀▀▀▀▀ ▀   ▀  ▀▀ ▀  ▀  ▀  <-

