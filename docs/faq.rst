============================
 Frequently asked questions
============================

Here we'll try to explain some reasons behind our decisions.

Why do we need a DSL?
=====================

    You can ignore convention.  You can't ignore the tool.

A DSL with lots of possibilities is hard to reason about and maintain.
A real programming language will go the same way without much
attention to the structure of your project.

Instead, we want ``stories`` DSL so limited, it forces the user to
explain his/her thoughts in a straightforward linear way.

All complexity will go to the implementation steps.  There you'll have
the whole power of the Python.

Why it is too magic?
====================

Careful programmers tend to avoid tools built on top of
meta-programming.  But we still use tools like dataclasses_, attrs_
and `django orm`_ because they improve developer experience a lot.

This is what ``stories`` try very hard:

    Bring the maximum value to your process, while keeping magic at
    the lowest possible minimum.

Why DSL does not use inheritance?
=================================

Many tools use like object relation mappers, web frameworks and task
queues use inheritance from some base class as the core of API.  We
saw a few problems with this approach.

First of all, you tend to put your business logic inside this
subclasses.  Fighting this evil was the initial idea behind
``stories`` library.

Also, this approach restricts your possibilities to manage your own
classes.  We want you to be free at the decisions where to put story
definition anywhere.  It is your right to place it inside Django
Model.

What is the best way to prototype my own DSL look and feel?
===========================================================

We receive a lot of complains and suggestions related to the DSL look
and feel.  We are open to all ideas!  Please, experiment with DSL
more!

If you want to try to build another DSL version with the same
semantics, here are the quickest way to prototype it:

1. There is ``examples`` module in tests, which contains all possible
   DSL expressions are written down.
2. Rewrite each expression in your version of the DSL.
3. Implement DSL inside ``stories`` module without touching a single
   line of tests.


Let us know if you stuck!  We can do the redesign together!

Why we need ``@argument`` decorator instead of function arguments?
==================================================================

For the simplicity of implementation inside ``@story`` decorator.
Otherwise, we will need to use ``inspect`` library to call the
function.

Can I use ``self`` instead of ``I`` argument?
=============================================

Yes, you are free to use whatever name you want.  But we keep this
convention in our documentation and examples to keep in mind that
``I``, ``self`` and ``ctx`` are three different things.

.. _dataclasses: https://docs.python.org/3/library/dataclasses.html
.. _attrs: https://www.attrs.org/
.. _django orm: https://docs.djangoproject.com/en/dev/topics/db/
