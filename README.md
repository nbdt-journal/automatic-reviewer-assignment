# Automatic Reviewer Assignment

ML Model to assign reviewers to your paper automatically!

## Backend

### Setup:

    Preferably use a virtual environment, which can be done through venv or miniconda. Following this, install the requirements.

    By venv:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    By conda:
    conda create -n <env_name> python=3.10 # specify environment name and python version
    conda activate <env_name>
    pip install -r requirements.txt

    Some users might face a problem with the installation of the requirements (especially psycopg-2). Please refer to this [issue](
    https://stackoverflow.com/questions/73088528/installing-pycopg2-gave-me-an-issue-in-ubuntu-22-4-pip3-version-22-2) to solve the problem.

### For the Postgres Database:

    Install Postgres on your system, follow the instructions [here](https://www.postgresql.org/download/).

    Create a user named 'postgres' with password 'postgres' in the postgres terminal. In Ubuntu, this terminal can be accessed by typing 'sudo -su postgres psql' in the terminal.

    Create a database named 'nfp' in postgres.

    Make a copy of the .env.example file and rename it to .env.

    If there is PG Admin installed in the system, it will be easy to administer and monitor the data using the platform.

### Run the development server:

    uvicorn main:app --reload to run the website

    
## Frontend:

### Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

We start with the `pages/index.js`. The page auto-updates as you edit the file.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.

We use [Tailwind CSS](https://tailwindcss.com/) for styling. The `styles` directory contains the global styles and the `tailwind.config.js` file contains the configuration for Tailwind CSS.

### Workflow

The workflow for the user interface can be understood as:
- The user enters the website and is greeted with the home page.
- The user can then log into their account or create a new account.
- The user can then upload a paper (pdf) or enter the text of the abstract after which the user can search for authors, journals or articles related to the particulr abstract.
- The user can then view the results of the search and select the authors, journals or articles that they want 