from lettuce import *
from radish.features import base, admin

# MODELS

@step(u'there are no things$')
def no_things(step):
    step.given('there is no Thing')

@step(u'there is a(?:| random) thing$')
def there_is_a_thing(step):
    step.given('there is an instance of Thing')

@step(u'there should be (\d+) things?$')
def should_have_n_things(step, count):
    step.given('there should be %%s instances of Thing' %% count)

# NAVIGATION

@step(u"I navigate to that thing page")
def i_navigate_to_that_thing_page(step):
    step.given('I navigate the page of that Thing')

# PAGE ELEMENTS

@step(u"I should see that thing's name")
def and_i_should_see_that_thing_s_name(step):
    step.given('I should see the name of that Thing')
