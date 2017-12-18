# AB-Kafka

Uses extended [Flask-Split extension](https://github.com/databootcampbr/flask-split) for `A/B testing`_ your web application. It
is a fork that send ab test to Kafka too.

More about _A/B testing: http://en.wikipedia.org/wiki/A/B_testing


## Installation

### Dependencies

The easiest way to install is cloning::

    git clone https://github.com/databootcampbr/ab-kafka.git

You will also need Redis as a datastore and Kafka as a Broker.

Using Docker for Redis::

    docker run --rm --name redis-server -p 6379:6379 -d redis:latest

Using Docker compose for Kafka. Inside cloned folder::

    cd ab-kafka
    docker-compose up -d


### Project

    pip install -r requirements.txt
    python main.py


## Configuration

The following configuration values exist for Flask-Split.  Flask-Split loads
these values from your main Flask config which can be populated in various
ways.

A list of configuration keys currently understood by the extension:

``REDIS_URL``
    The database URL that should be used for the Redis connection. Defaults to
    ``'redis://localhost:6379'``.

``KAFKA_SERVERS``
    The broker URL that should be used for the Kafka send events. Defaults to
    ``'localhost:9092'``.

``KAFKA_TOPIC``
    The topic for Kafka send events. Defaults to
    ``'ab_test'``.

``SPLIT_ALLOW_MULTIPLE_EXPERIMENTS``
    If set to `True` Flask-Split will allow users to participate in multiple
    experiments.

    If set to `False` Flask-Split will avoid users participating in multiple
    experiments at once.  This means you are less likely to skew results by
    adding in more  variation to your tests.

    Defaults to `False`.

``SPLIT_IGNORE_IP_ADDRESSES``
    Specifies a list of IP addresses to ignore visits from.  You may wish to
    use this to prevent yourself or people from your office from skewing the
    results.

    Defaults to ``[]``, i.e. no IP addresses are ignored by default.

``SPLIT_ROBOT_REGEX``
    Flask-Split ignores visitors that appear to be robots or spider in order to
    avoid them from skeweing any results. Flask-Split detects robots and
    spiders by comparing the user agent of each request with the regular
    expression in this setting.

    Defaults to::

        r"""
        (?:i)\b(
            Baidu|
            Gigabot|
            Googlebot|
            libwww-perl|
            lwp-trivial|
            msnbot|
            SiteUptime|
            Slurp|
            WordPress|
            ZIBB|
            ZyBorg
        )\b
        """

``SPLIT_DB_FAILOVER``
    If set to `True` Flask-Split will not let :meth:`ab_test` or
    :meth:`finished` to crash in case of a Redis connection error.  In that
    case :meth:`ab_test` always delivers the first alternative i.e. the
    control.

    Defaults to `True`.


## Usage

Access http://127.0.0.1:5000



