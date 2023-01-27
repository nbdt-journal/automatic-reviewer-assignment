# Automatic Reviewer Assignment

ML Model to assign reviewers to your paper automatically!

## Backend:

### Setup:

    Preferably use a virtual environment
    This can be done through venv or miniconda

    By venv:
    python3 -m venv venv
    source venv/bin/activate

    By conda:
    conda create -n <env_name> python=3.10
    conda activate <env_name>

    Install the requirements:
    pip install -r requirements.txt

    Some users might face a problem with the installation of the requirements (especially psycopg-2). Users can then refer to this [link](
    https://stackoverflow.com/questions/73088528/installing-pycopg2-gave-me-an-issue-in-ubuntu-22-4-pip3-version-22-2) to solve the problem.

### For the Postgres Database:

    Install Postgres on your system, follow the instructions [here](https://www.postgresql.org/download/).

    Create a user named 'postgres' with password 'postgres' in the postgres terminal. In Ubuntu, this terminal can be accessed by typing 'sudo -su postgres psql' in the terminal.

    Create a database named 'nfp' in postgres.

    Make a copy of the .env.example file and rename it to .env.

    If there is PG Admin installed in the system, it will be easy to administer and monitor the data using the platform.

Run the development server:

    uvicorn main:app --reload to run the website

 
## Frontend:

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

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

### Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!
