
# npm依赖
```shell
npm i --save gitalk
```

# GitHub Workflow
```shell
name: Sync, Build and Deploy

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'  # 每天凌晨2点运行
  workflow_dispatch:  # 允许手动触发

jobs:
  sync-build-and-deploy:
    runs-on: ubuntu-latest
    
    env:
      YUQUE_ACCESS_TOKEN: 
      OAUTH_CLIENT_ID: 
      OAUTH_CLIENT_SECRET: 

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run app.py
      run: python app.py

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'

    - name: Install Node.js dependencies
      run: npm install

    - name: Build VitePress site
      run: npm run build

    - name: Push to yuque-sync repository
      run: |
        git config --global user.name 'GitHub Actions'
        git config --global user.email 'github-actions@github.com'
        git remote set-url origin git@github.com:Meidanlong/yuque-sync.git
        git add .
        git commit -m "Auto-sync and build"
        git push --force origin HEAD:${{ env.REPO_BRANCH }}
      env:
        GH_TOKEN: ${{ secrets.GH_TOKEN }}

    - name: Push to GitHub Pages repository
      run: |
        cd .vitepress/dist
        git init
        git config user.name 'GitHub Actions'
        git config user.email 'github-actions@github.com'
        git add .
        git commit -m "Deploy to GitHub Pages"
        git push --force git@github.com:Meidanlong/meidanlong.github.io.git HEAD:gh-pages
      env:
        GH_TOKEN: ${{ secrets.GH_TOKEN }}

```