import subprocess


def get_dependencies(package_name):
    process = subprocess.Popen(['apt-cache', 'depends', package_name], stdout=subprocess.PIPE)
    output, error = process.communicate()

    dependencies = []
    for line in output.decode().split('\n'):
        if 'Depends' in line:
            dependencies.append(line.split(':')[1].strip())

    return dependencies
