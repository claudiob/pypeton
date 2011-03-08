Feature: Things
  In order to add, remove and edit things
  As an administrator
  I want to do it through the CMS

  Scenario: Adding a thing
    Given there are no things
    And I am logged in as an admin
    When I click the "Things" link
    And I click the "Add thing" link
    And I fill the "name" field with "yellow car"
    And I click the "Save" button
    Then there should be 1 thing

  Scenario: Displaying a thing's page
    Given there is a thing
    When I navigate to that thing page
    Then I should see that thing's name

