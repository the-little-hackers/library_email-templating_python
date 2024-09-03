# MIT License
#
# Copyright (C) 2024 The Little Hackers.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import annotations

from os import PathLike
from typing import Any
from typing import Iterable

from thelittlehackers.utils import any_utils
from thelittlehackers.utils import string_utils


# class EmailTemplate:
#     """
#     Template for generating the content of localized emails.
#
#     An email can be localized in several languages (locales).  Each
#     localization corresponds to a file named after the locale in which
#     the content is written (RFC 4646).
#
#     A locale is expressed by a ISO 639-3 alpha-3 code element, optionally
#     followed by a dash character `-` and a ISO 3166-1 alpha-2 code.  For
#     example: "eng" (which denotes a standard English), "eng-US" (which
#     denotes an American English).
#
#     For instance:
#
#     /absolute/path/to/template/folder
#     ├── eng.txt
#     ├── fra.txt
#     └── vie.txt
#
#     This class uses Jinja template engine for rendering email content.
#     """
#     class NotRenderedError(Exception):
#         """
#         Signal that the email template has not been rendered with placeholders
#         """
#
#     def __init__(
#             self,
#             template_path: str,
#             locale: Locale = DEFAULT_LOCALE,
#             template_file_extension: str = '.txt'):
#         """
#         Create a new email template instance
#
#
#         :param template_path: The absolute path of the folder containing the
#             localized template files.
#
#         :param locale: The locale to generate email content.
#
#         :param template_file_extension: The extension of the localized
#             template files.
#         """
#         self.__template_path = template_path
#         self.__template_file_extension = template_file_extension
#
#         self.__environment = jinja2.Environment(loader=jinja2.FileSystemLoader(self.__template_path))
#         self.__template = self.__environment.get_template(self.__get_template_file_name(locale))
#         self.__content = None
#
#     def __get_template_file_name(self, locale: Locale = DEFAULT_LOCALE) -> str:
#         """
#         Return the absolute path and file name of the template for the
#         specified locale
#
#         If no template exists for the specified locale, the function returns
#         the absolute path and name of the template file for the default locale
#         `Locale.DEFAULT_LOCALE`.
#
#
#         :param locale: The locale of the desired template.
#
#
#         :return: The absolute path and file name of the template file for the
#             specified locale or the default locale
#         """
#         if not isinstance(locale, Locale):
#             raise ValueError("The argument `locale` must be an object `Locale`")
#
#         template_file_name = f'{locale.to_string()}{self.__template_file_extension}'
#         template_file_path_name = os.path.join(self.__template_path, template_file_name)
#
#         if not os.path.exists(template_file_path_name):
#             if locale == DEFAULT_LOCALE:
#                 raise FileNotFoundError(f'No email template defined for the default locale "{DEFAULT_LOCALE}"')
#             return self.__get_template_file_name(DEFAULT_LOCALE)
#
#         return template_file_name
#
#     def render(self, **kwargs) -> str:
#         """
#         Render the content of the email in the specified locale
#
#
#         :param kwargs: Variables which values replace the corresponding
#             placeholders defined in the email content.
#
#
#         :return: The rendered template.
#         """
#         self.__content = self.__template.render(**kwargs)
#         return self.__content
#
#     @property
#     def content(self) -> str:
#         """
#         Return the content of the email that has been rendered
#
#
#         :return: The rendered content of the email.
#
#
#         :raise NotRenderedError: If the function `render` has not been called
#             yet.
#         """
#         if self.__content is None:
#             raise self.NotRenderedError("This email template must be rendered first")
#
#         return self.__content


# class EmailHtmlTemplate(EmailTemplate):
#     """
#     Template for generating the content of localized HTML emails
#
#     The subject of the email corresponds to the title of the HTML template
#     document.
#     """
#     class UndefinedTitleTagError(Exception):
#         """
#         Signal that the HTML document has not tag `title` defined.
#         """
#
#     REGEX_PATTERN_HTML_TITLE = r'<title>(.*)<\/title>'
#     REGEX_HTML_TITLE = re.compile(REGEX_PATTERN_HTML_TITLE)
#
#     @staticmethod
#     def _cleanse_subject(subject):
#         """
#         Cleanse the content of the subject
#
#         Remove leading, trailing, and redundant spaces characters.  Capitalize
#         the first word of the subject.
#
#
#         :param subject: A string representing the subject of an email.
#
#
#         :return: The cleansed subject.
#         """
#         words = subject.split()
#         if len(words) > 0:
#             words[0] = words[0].capitalize()
#             subject = ' '.join(words)
#         return subject
#
#     def __init__(
#             self,
#             template_path: str,
#             locale: Locale = DEFAULT_LOCALE):
#         """
#         Create a new email template instance
#
#
#         :param template_path: The absolute path of the folder containing the
#             localized template files.
#
#         :param locale: The locale to generate email content.
#         """
#         super().__init__(template_path, locale=locale, template_file_extension=".html")
#         self.__subject = None
#
#     @classmethod
#     def __get_html_title(cls, content: str) -> str:
#         """
#         Return the title of the HTML document
#
#
#         :param content: The content of a HTML document.
#
#
#         :return: The value of the tag `title` of the HTMl document.
#
#
#         :raise UndefinedTitleTagError: If the HTML document doesn't contain
#             the HTML tag `title`.
#         """
#         match = cls.REGEX_HTML_TITLE.search(content)
#         if not match:
#             raise cls.UndefinedTitleTagError("The HTML content has no title defined")
#
#         title = match.group(1)
#         return title
#
#     @property
#     def subject(self) -> str:
#         """
#         Return the content of the email that has been rendered
#
#
#         :return: The rendered content of the email.
#
#
#         :raise NotRenderedError: If the function `render` has not been called
#             yet.
#
#         :raise UndefinedTitleTagError: If the HTML document doesn't contain
#             the HTML tag `title`.
#         """
#         if self.__subject is None:
#             self.__subject = self._cleanse_subject(
#                 self.__get_html_title(self.content))
#
#         return self.__subject


class Mailbox:
    """
    Represents an email mailbox with an associated email address and
    optional name.

    The ``Mailbox`` class encapsulates an email address and an optional
    name, typically representing the owner of the mailbox.  It provides
    methods for retrieving these values and a string representation of the
    mailbox in the format ``"Name" <email_address>``.
    """
    def __init__(
            self,
            email_address: str,
            name: str = None
    ):
        """
        Create a `Mailbox` object.


        :param email_address: Electronic mail address of the mailbox.

        :param name: The name of the owner of this mailbox, generally the
            full name of a person.


        :raise ValueError: If the input string is not a valid email address.
        """
        self.__name = name and name.strip()
        self.__email_address = string_utils.string_to_email_address(email_address)

    def __str__(self) -> str:
        return f'"{self.__name}" <{self.__email_address}>'

    @property
    def email_address(self) -> str:
        """
        Return the email address associated with this mailbox.


        :return: The email address as a string.
        """
        return self.__email_address

    @staticmethod
    def from_json(payload: dict) -> Mailbox | None:
        """
        Create a `Mailbox` instance from a JSON-like dictionary.

        This method parses a dictionary containing the keys ``email_address``
        and ``name`` to create a ``Mailbox`` object.


        :param payload: A dictionary containing the keys ``email_address`` and
            optionally ``name``.


        :return: A ``Mailbox`` instance, or ``None`` if the payload is ``None``.


        :raise ValueError: If the value of the key ``email_address`` is not a
            valid email address.
        """
        return payload and Mailbox(
            payload['email_address'],
            name=payload.get('name')
        )

    @property
    def name(self) -> str:
        return self.__name


class Email:
    """
    Represent a message to be sent as an electronic mail to recipient(s).
    """
    def __init__(
            self,
            author: Mailbox,
            recipients: Mailbox | Iterable[Mailbox],
            subject: str,
            bcc_recipients: Mailbox | Iterable[Mailbox] = None,
            cc_recipients: Mailbox | Iterable[Mailbox] = None,
            html_content: str = None,
            text_content: str = None,
            attached_files: PathLike | Iterable[PathLike] = None
    ):
        """
        Initialize an ``Email`` instance.


        :param author: A `Mailbox` object representing the author, with the
            email address of the mailbox to which the author of the message
            suggests that replies be sent.

        :param recipients: An object or a collection of objects `Mailbox`
            representing the recipient(s) of the message.

        :param subject: A short string identifying the topic of the message.

        :param bcc_recipients: An object or a collection of objects `Mailbox`
            representing the Blind Carbon Copy (BCC) recipient(s) of the
            message.

            The other recipients of the message won’t be able to see that these
            BBC recipients have been sent a copy of the email.

        :param cc_recipients: An object or a collection of objects `Mailbox`
            representing the Carbon Copy (CC) recipient(s) of the message.

            Using CC is more a matter of etiquette than anything. The general
            rule is that the "To" field is reserved for the main recipients of
            an email. Other interested parties can be included as a CC so they
            can have their own copy of the email.

        :param html_content: The HTML body of the message.

        :param text_content: The plain text body of the message.

        :param attached_files: A string or a collection of strings
            corresponding to the full path and name of the files to attached
            to this message.
        """
        if any_utils.is_empty_or_none(html_content) and any_utils.is_empty_or_none(text_content):
            raise ValueError("Empty content")

        self.__author = author
        self.__recipients = self.__build_list(recipients)
        self.__cc_recipients = self.__build_list(cc_recipients)
        self.__bcc_recipients = self.__build_list(bcc_recipients)
        self.__subject = subject
        self.__text_content = text_content
        self.__html_content = html_content
        self.__attached_files = self.__build_list(attached_files)

    @staticmethod
    def __build_list(value: Any) -> list | None:
        if value is None:
            return None

        return value if isinstance(value, Iterable) else list(value)

    @staticmethod
    def __parse_mailboxes_from_json(payload: dict | Iterable[dict]) -> Iterable[Mailbox] | None:
        if not payload:
            return None

        # noinspection PyTypeChecker
        # :note: `Mailbox.from_json` could possibly return `None` if payload was
        #     `None`, which is not the case in this context.
        recipients = list(Mailbox.from_json(payload)) if isinstance(payload, dict) \
            else [
                Mailbox.from_json(recipient_json)
                for recipient_json in payload
            ]

        return recipients

    @property
    def attached_files(self) -> Iterable[PathLike] | None:
        """
        Return the list of files attached to this email.


        :return: An iterator of `PathLike` objects representing the attached
            files.
        """
        return self.__attached_files

    @property
    def author(self) -> Mailbox:
        """
        Return the author (sender) of the email.


        :return: The `Mailbox` object representing the email's author.
        """
        return self.__author

    @property
    def bcc_recipients(self) -> Iterable[Mailbox] | None:
        """
        Return the Blind Carbon Copy (BCC) recipient(s) of the email.


        :return: An iterable of `Mailbox` objects representing the BCC
            recipients, or ``None`` if there are no BCC recipients.
        """
        return self.__bcc_recipients

    @property
    def cc_recipients(self) -> Iterable[Mailbox] | None:
        """
        Return the Carbon Copy (CC) recipient(s) of the email.


        :return: An iterable of `Mailbox` objects representing the CC
            recipients, or ``None`` if there are no CC recipients.
        """
        return self.__cc_recipients

    @property
    def content(self) -> str:
        """
        Return the body of the email, preferring HTML content if available.


        :return: A string containing the email's body, either HTML or plain
            text.
        """
        return self.__html_content or self.__text_content

    @classmethod
    def from_json(cls, payload):
        if payload is None:
            return None

        author = Mailbox.from_json(payload['author'])
        subject = payload['subject']
        recipients = cls.__parse_mailboxes_from_json(payload['recipients'])
        cc_recipients = cls.__parse_mailboxes_from_json(payload.get('cc_recipients'))
        bcc_recipients = cls.__parse_mailboxes_from_json(payload.get('bcc_recipients'))
        html_content = payload.get('html_content')
        text_content = payload.get('text_content')

        return Email(
            author,
            recipients,
            subject,
            bcc_recipients=bcc_recipients,
            cc_recipients=cc_recipients,
            html_content=html_content,
            text_content=text_content
        )

    @property
    def html_content(self) -> str | None:
        """
        Return the HTML body of the email.


        :return: A string containing the HTML content, or ``None`` if not
            provided.
        """
        return self.__html_content

    @property
    def recipients(self) -> Iterable[Mailbox]:
        """
        Return the primary recipients of the email.


        :return: An iterable of ``Mailbox`` objects representing the primary
            recipients.
        """
        return self.__recipients

    @property
    def subject(self) -> str:
        """
        Return the subject of the message.

        The subject is the headline of the email.  It's a brief summary or
        title of the email's content. It is displayed in the recipient's inbox,
        usually right next to or below the sender's name, and helps the
        recipient understand the purpose or main idea of the email before
        opening it.


        :return: A string representing the email's subject.
        """
        return self.__subject

    @property
    def text_content(self) -> str | None:
        """
        Return the plain text body of the email.


        :return: A string containing the plain text content, or ``None`` if
            not provided.
        """
        return self.__text_content
