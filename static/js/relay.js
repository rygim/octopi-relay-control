$(function() {
    function RelayViewModel(parameters) {
        var self = this;

        self.toggleRelay = function(channel) {
            console.log("toggleRelay");
            $.ajax({
                url: "/plugin/relay/toggleRelay",
                type: "POST",
                dataType: "json",
                data: {
                    toggleRelay: true
                },
                contentType: "application/json; charset=UTF-8",
                success: function(data) {
                    console.log("back")
                }
            });

            return false;
        };
    }

    ADDITIONAL_VIEWMODELS.push([
        RelayViewModel,
        ["loginStateViewModel", "settingsViewModel"],
        ["#navbar_toggle_power"]
    ]);
});
