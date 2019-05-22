// Adds selected golfer to group
function addGroup(groupId) {
    var noGroup = document.getElementById("nogroup");
    var values = noGroup.selectedOptions;
    var group = document.getElementById(groupId);
    for (i = 0; i < values.length;) {
        group.add(values.item(i));
    }
    removeSelection(groupId);
}

// Removes selected golfer from group
function removeGroup(groupId) {
    var noGroup = document.getElementById("nogroup");
    var group = document.getElementById(groupId);
    var values = group.selectedOptions;
    for (i = 0; i < values.length;) {
        noGroup.add(values.item(i));
    }
    removeSelection("nogroup");
}

// Removes all golfers from a group
function removeGroupAll(groupId) {
    var noGroup = document.getElementById("nogroup");
    var group = document.getElementById(groupId);
    for (i = 0; i < group.length;) {
        noGroup.add(group.item(i));
    }
    removeSelection("nogroup");
}

// Deselects golfers that were moved
function removeSelection(groupId) {
    var group = document.getElementById(groupId);
    for (var i = 0; i < group.options.length; i++) {
        group.options[i].selected = false;
    }
}

// Selects all groups on page submit
function selectAll() {
    var group1 = document.getElementById("group1");
    var group2 = document.getElementById("group2");
    var group3 = document.getElementById("group3");
    var group4 = document.getElementById("group4");
    var group5 = document.getElementById("group5");
    var group6 = document.getElementById("group6");

    for (var i = 0; i < group1.options.length; i++) {
        group1.options[i].selected = true;
    }

    for (var i = 0; i < group2.options.length; i++) {
        group2.options[i].selected = true;
    }

    for (var i = 0; i < group3.options.length; i++) {
        group3.options[i].selected = true;
    }

    for (var i = 0; i < group4.options.length; i++) {
        group4.options[i].selected = true;
    }

    for (var i = 0; i < group5.options.length; i++) {
        group5.options[i].selected = true;
    }

    for (var i = 0; i < group6.options.length; i++) {
        group6.options[i].selected = true;
    }
}