function closeLauncher(launchers) {
    console.log("Closing launcher");
    console.log(launchers[0]);
    launchers[0].close();
}


function findDevXWorkshopCommand() {
    // Access the global JupyterLab app object
    const app = window.jupyterapp;

    // Find all widgets in the shell that are Launcher widgets
    var launchers = Array.from(app.shell.widgets('main')).filter(w =>
        w.id && w.id.includes('launcher')
    );
    var createdLauncher = false;

    if (launchers.length == 0) {
        console.log("No launchers found, creating one");
        app.commands.execute("launcher:create");
        launchers = Array.from(app.shell.widgets('main')).filter(w =>
            w.id && w.id.includes('launcher')
        );
        createdLauncher = true;
    }

    // Search through all launchers for the target item
    for (const launcher of launchers) {
        // Each launcher widget has a model with the launcher items
        var model = launcher.content?.model;
        if (model) {
            // Items are grouped into sections
            const sections = model.items();
            for (const item of sections) {
                // Check if this item matches our criteria
                if (item.category === "NVIDIA DevX Workshops" && item.rank === 0) {
                    if (createdLauncher) {
                        closeLauncher(launchers);
                    }
                    return item.command;
                }
            }
        }
    }

    // Return null if not found
    if (createdLauncher) {
        closeLauncher(launchers);
    }
    return null;
}

var command = findDevXWorkshopCommand();
window.jupyterapp.commands.execute(command);

