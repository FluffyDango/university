<?php

// Load composer dependencies
require_once 'vendor/autoload.php';

// settings
date_default_timezone_set('Europe/Vilnius');

$baseUri = '/';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();
$dbHost = $_ENV['DB_HOST'];
$dbName = $_ENV['DB_NAME'];
$dbUser = $_ENV['DB_USER'];
$dbPassword = $_ENV['DB_PASSWORD'];
// Database
$pdo = new PDO("pgsql:host={$dbHost};dbname={$dbName}", $dbUser, $dbPassword);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Mapping PHP errors to exceptions
// function exception_error_handler($errno, $errstr, $errfile, $errline) {
//     throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
// }
// set_error_handler("exception_error_handler");

// Backends
$authBackend      = new Sabre\DAV\Auth\Backend\PDO($pdo);
$authBackend->setRealm('pullout');
$principalBackend = new Sabre\DAVACL\PrincipalBackend\PDO($pdo);
$carddavBackend   = new Sabre\CardDAV\Backend\PDO($pdo);

$nodes = [
    new Sabre\DAVACL\PrincipalCollection($principalBackend),
    new Sabre\CardDAV\AddressBookRoot($principalBackend, $carddavBackend),
];

// The object tree needs in turn to be passed to the server class
$server = new Sabre\DAV\Server($nodes);
$server->setBaseUri($baseUri);

// Plugins

// Authentication plugin
$server->addPlugin(new Sabre\DAV\Auth\Plugin($authBackend));
$aclPlugin = new \Sabre\DAVACL\Plugin();
$aclPlugin->adminPrincipals[] = 'principals/admin';
$server->addPlugin($aclPlugin);
// Ability to open in browser
$server->addPlugin(new Sabre\DAV\Browser\Plugin());
// CardDav plugin
$server->addPlugin(new Sabre\CardDAV\Plugin());
// Syncing plugin
$server->addPlugin(new Sabre\DAV\Sync\Plugin());

$server->start();
