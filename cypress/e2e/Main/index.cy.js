/// <reference types="cypress" />

context("Main React page", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("renders page correctly", () => {
    cy.get('h1').contains("Stationery Shop");
  });
});
