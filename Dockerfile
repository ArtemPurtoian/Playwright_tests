FROM python:3.12.4

RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libasound2 \
    fonts-liberation \
    xvfb \
    xauth \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir playwright==1.55.0 && \
    python -m playwright install --with-deps

WORKDIR /Playwright_tests

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["xvfb-run", "-a", "pytest", "-vv", "-s"]
