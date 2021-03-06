# Copyright 2012, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.shortcuts import render
from graph.models import Category, Course
from documents.models import Document

def home(request):

    explicit_followed = request.user.get_profile().follow.all()
    followed = set()
    for node in explicit_followed:
        followed.add(node)
        followed.update(node.descendants_set())

    followed_courses = filter(lambda n: n.classBasename() == 'Course',followed)

    return render(request, "home.html",
                  {"followed_courses": list(followed_courses)})