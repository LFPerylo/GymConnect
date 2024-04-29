const { defineConfig } = require("cypress");

module.exports = defineConfig({
  projectId: 'hr2nvq',
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
