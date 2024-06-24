from fastapi import Request
from database import new_session
from models import Link, LinkAccess
from schemas import SRef
from settings import logger
from uuid import UUID


class RefRepository:
    @classmethod
    def get_next_ref(cls, link_id: UUID, request: Request):
        session = new_session()
        try:
            # Retrieve the link from the database
            link = session.query(Link).filter_by(id=link_id).first()
            if not link:
                return None

            # Extract client IP address from request
            client_ip = request.client.host

            # Check if this IP has accessed this link
            existing_access = session.query(LinkAccess).filter_by(link_id=link_id, ip_address=client_ip).first()

            # If the IP has accessed the link, return the current ref without incrementing
            if existing_access:
                logger.debug(f'IP {client_ip} has already accessed link {link_id}')
                return cls._get_current_ref(existing_access, link)

            # Update the ref index
            next_ref = cls._increment_ref_index(link)
            logger.debug(f'new ref_index: {link.ref_index}')

            # Record the access
            new_access = LinkAccess(link_id=link_id, ip_address=client_ip, ref_index=link.ref_index)
            session.add(new_access)
            session.commit()

            return next_ref
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()

    @classmethod
    def _get_current_ref(cls, existing_access, link):
        refs = link.refs
        ref_index = existing_access.ref_index
        logger.debug(f'Current ref index: {ref_index}')
        logger.debug(f'refs: {refs}, length: {len(refs)}')
        return SRef(id=refs[ref_index].id, url=refs[ref_index].url) if refs else None

    @classmethod
    def _increment_ref_index(cls, link):
        refs = link.refs
        ref_index = link.ref_index
        next_ref = refs[ref_index]
        link.ref_index = (ref_index + 1) % len(refs)
        return SRef(id=next_ref.id, url=next_ref.url) if refs else None
