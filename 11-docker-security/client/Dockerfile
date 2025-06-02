FROM alpine
RUN apk add --no-cache curl
COPY curl.sh /curl.sh
RUN chmod +x /curl.sh
CMD ["/curl.sh"]