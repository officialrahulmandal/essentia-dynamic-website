Essentia
==============================

__Version:__ 0.0.0

backend + cms + frontend of essentia 

## Getting up and running

Minimum requirements: **pip, fabric, python3, node, npm, yarn  & [postgres][install-postgres]**, setup is tested on Mac OSX only.


```
brew install postgres python3
[sudo] pip install fabric
```

[install-postgres]: http://www.gotealeaf.com/blog/how-to-install-postgresql-on-a-mac

In your terminal, type or copy-paste the following:

    git clone git@github.com:essentia/essentia-web.git; cd essentia-web; fab init

Go grab a cup of coffee, we bake your hot development machine.

Useful commands:

- `fab serve` - start [django server](http://localhost:8000/)
- `fab deploy_docs` - deploy docs to server
- `fab test` - run the test locally with ipdb

- `fab watch` - build dev staticfiles and start [node server](http://localhost:3000/)
- `fab build` - build dev staticfiles
- `fab prod build` - build production staticfiles

**NOTE:** Checkout `fabfile.py` for all the options available and what/how they do it.


## Deploying Project

The deployment are managed via travis, but for the first time you'll need to set the configuration values on each of the server.

Check out detailed server setup instruction [here](docs/backend/server_config.md).

## How to release Essentia

Execute the following commands:

```
git checkout master
fab test
bumpversion patch  # 'patch' can be replaced with 'minor' or 'major'
git push origin master
git push origin master --tags
git checkout qa
git rebase master
git push origin qa
```

## Contributing

Golden Rule:

> Anything in **master** is always **deployable**.

Avoid working on `master` branch, create a new branch with meaningful name, send pull request asap. Be vocal!

Refer to [CONTRIBUTING.md][contributing]

[contributing]: http://github.com/essentia/essentia-web/tree/master/CONTRIBUTING.md
