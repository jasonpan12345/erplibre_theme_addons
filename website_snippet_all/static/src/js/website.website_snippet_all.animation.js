odoo.define("website_snippet_all.animation", function (require) {
    "use strict";

    var sAnimation = require("website.content.snippets.animation");

    sAnimation.registry.website_snippet_all = sAnimation.Class.extend({
        selector: ".o_website_snippet_all",

        start: function () {
            var self = this;
            var def = this._rpc({
                route: "/website_snippet_all/helloworld",
            }).then(function (data) {
                if (data.error) {
                    return;
                }

                if (_.isEmpty(data)) {
                    return;
                }

                var data_json = data;
                var hello = data_json["hello"];
                self.$(".website_snippet_all_value").text(hello);
            });

            return $.when(this._super.apply(this, arguments), def);
        },
    });
});
