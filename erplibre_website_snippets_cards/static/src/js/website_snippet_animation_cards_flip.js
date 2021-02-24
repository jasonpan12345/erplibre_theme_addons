odoo.define('erplibre_website_snippets_cards.animation_cards_flip', function (require) {
  'use strict';

  var sAnimation = require('website.content.snippets.animation');

  sAnimation.registry.erplibre_website_snippets_cards_flip = sAnimation.Class.extend({
    selector: '.o_cards_flip',
    read_events: {
      'click .flippable': '_toggleFlip',
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _toggleFlip: function (ev) {
      var card = ev.currentTarget;
      var className = "flipped";
      if (card.classList.contains(className)) {
        card.classList.remove(className);
      } else {
        card.classList.add(className);
      }
    },
  })
});
