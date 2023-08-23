# Using Webpack
Webpack is set up to watch the src directory for changes. 

Start Webpack with:

```bash
npm run build
```

Webpack will automatically recompile the CSS any time a change is made to any file in the src directory.

# Requirements
Webpack requires node and npm

Install the webpack dependencies by running this command from the webpack directory:

```bash
npm install
```

# Linux servers do not come with node or npm installed

Install Node and NPM with the following commands

```bash
yum install nodejs
yum install npm
```

You can upgrade node by locating the rh-nodejs package with the latest version. This is version 14 on RHEL 7.9

```bash
yum search rh-node
```