As we were told to do, my goal was to keep my API part and CLI part separate.

In my API, I've this structre

projman
--src
  --pm
  --projman
    --common
    --create
    --delete
    --list_projects
    --delete

So for API(projman/projman) I've
All common functions are under common module like
	Getting types of project we can create, like houdini, maya
	Getting if we've yaml config files available for each type or not
	Getting project location

and other modules were used for creating,deleting and listing projects.

We only need to import the API(projman) in pm file and all necessary functions for managing project will be available under the projman namespace, so we don't have to
import individual modules under API.

I've only one concern, I've tested my code on windows system. So it might fail for some linux specific parts,
although I've taken care to not let this happen but I can't be sure. So please take into consideration for any such fails.
	 
