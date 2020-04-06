#include "Poco/Net/HTTPRequest.h"
#include "Poco/Net/HTTPSClientSession.h"
#include "Poco/Net/HTTPResponse.h"
#include "Poco/Net/Context.h"
#include "Poco/Path.h"
#include "Poco/URI.h"
#include "iostream"
#include "responseparser.h"


using namespace std;
using Poco::Net::HTTPSClientSession;
using Poco::Net::HTTPRequest;
using Poco::Net::HTTPResponse;
using Poco::Net::HTTPMessage;
using Poco::Net::Context;
using Poco::Path;
using Poco::URI;

int main(int argc, char** argv)
{
    URI uri("https://reisapi.ruter.no/line/getstopsbylineid/9110");
    string path(uri.getPathAndQuery());

    // HTTPS
    const Poco::Net::Context::Ptr context = new Poco::Net::Context(
        Poco::Net::Context::CLIENT_USE, "", "", "",
        Poco::Net::Context::VERIFY_NONE, 9, false,
    "ALL:!ADH:!LOW:!EXP:!MD5:@STRENGTH");

    HTTPRequest request(HTTPRequest::HTTP_GET, path, HTTPMessage::HTTP_1_1);
    HTTPSClientSession session( uri.getHost(),uri.getPort(), context);

    session.sendRequest(request);
    HTTPResponse response;    

    responseparser(session, response);
}