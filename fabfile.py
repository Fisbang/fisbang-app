from fabric.api import *
import time, json

app_name = 'fisbang'

num_keep_releases = 5

file_list = [   'fisbang/app/*',
                'fisbang/api/*',
                'fisbang/models/*',
                'fisbang/static/*',
                'fisbang/templates/*',
                'fisbang/helpers/*',
                'fisbang/*.py',
                'conf/uwsgi.ini',
                'conf/settings.conf.sample',
                'migrations/*',
                'manage.py',
                'wsgi.py',
                'requirements.txt'   ]

def prod():
    f = open('conf/fab_env.json', 'r')
    env_stuff = json.load(f)
    f.close()
    env.hosts = env_stuff['hosts']
    env.user = env_stuff['user']
    env.key_filename = env_stuff['key']
    env.app_path = '/var/www/app.fisbang.com'
    env.base_url = 'app.fisbang.com'
    env.config_file_path = '/var/www/app.fisbang.com/config/settings.cfg'

def pack():
    filelist = ' '.join(file_list)
    local('tar czf dist/{}.tar.gz {}'.format(app_name, filelist))

def deploy():
    # new source distribution
    pack()

    # upload it to server
    run('mkdir -p {}/tmp'.format(env.app_path))
    put('dist/{}.tar.gz'.format(app_name), '{}/tmp'.format(env.app_path))

    # extract it to folder
    timestamp = time.strftime("%Y%m%d%H%M%S")
    deploy_path = '{}/releases/{}'.format(env.app_path, timestamp)
    run('mkdir -p {}'.format(deploy_path))

    with cd('{}'.format(env.app_path)):
        run('tar xzf tmp/{}.tar.gz -C {}'.format(app_name, deploy_path))
        run('ln -nfs {} current'.format(deploy_path))

    with cd('{}/current'.format(env.app_path)):
        run('virtualenv venv; source venv/bin/activate; pip install -r requirements.txt')
        run('echo "env = FISBANG_SETTINGS={}" >> conf/uwsgi.ini'.format(env.config_file_path))
        run('echo "chdir = {}/current" >> conf/uwsgi.ini'.format(env.app_path))
        run('echo "logto = /var/log/uwsgi/{}.log" >> conf/uwsgi.ini'.format(env.base_url))
        run('echo "virtualenv = {}/current/venv" >> conf/uwsgi.ini'.format(env.app_path))

    run('service uwsgi restart')
    # cleanup
    with cd('{}/releases'.format(env.app_path)):
        run('rm -r `ls -r | tail -n +{}`;true'.format(num_keep_releases + 1))
